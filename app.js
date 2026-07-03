const REPO = {
  owner: 'Dhruv-jain-dev',
  name: 'AGENTIC_AI_TRAINING',
  branch: 'main',
};

const FALLBACK_REPORTS = Array.isArray(window.REPORTS) ? window.REPORTS : [];
const state = {
  reports: [],
  filter: '',
  loading: true,
  source: 'GitHub',
};

const $ = selector => document.querySelector(selector);
const API_ROOT = `https://api.github.com/repos/${REPO.owner}/${REPO.name}`;
const RAW_ROOT = `https://raw.githubusercontent.com/${REPO.owner}/${REPO.name}/${REPO.branch}`;
const BLOB_ROOT = `https://github.com/${REPO.owner}/${REPO.name}/blob/${REPO.branch}`;
const TREE_URL = `${API_ROOT}/git/trees/${REPO.branch}?recursive=1`;

function escapeHtml(value = '') {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function inlineMarkdown(text = '') {
  const safe = escapeHtml(text);
  return safe
    .replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`(.+?)`/g, '<code>$1</code>');
}

function markdownToHtml(markdown = '') {
  const lines = String(markdown).split(/\r?\n/);
  let html = '';
  let listOpen = false;
  let tableOpen = false;
  let codeOpen = false;

  const closeBlocks = () => {
    if (listOpen) {
      html += '</ul>';
      listOpen = false;
    }
    if (tableOpen) {
      html += '</tbody></table>';
      tableOpen = false;
    }
  };

  for (const rawLine of lines) {
    const line = rawLine.trimEnd();

    if (line.startsWith('```')) {
      closeBlocks();
      if (codeOpen) {
        html += '</code></pre>';
        codeOpen = false;
      } else {
        html += '<pre><code>';
        codeOpen = true;
      }
      continue;
    }

    if (codeOpen) {
      html += `${escapeHtml(rawLine)}\n`;
      continue;
    }

    if (/^\|/.test(line)) {
      if (/^\|[\s|:-]+\|?$/.test(line)) {
        continue;
      }
      closeBlocks();
      if (!tableOpen) {
        html += '<table><tbody>';
        tableOpen = true;
      }
      const cells = line.split('|').slice(1, -1).map(cell => `<td>${inlineMarkdown(cell.trim())}</td>`);
      html += `<tr>${cells.join('')}</tr>`;
      continue;
    }

    if (tableOpen) {
      html += '</tbody></table>';
      tableOpen = false;
    }

    const heading = line.match(/^(#{1,3})\s+(.+)/);
    if (heading) {
      closeBlocks();
      const level = heading[1].length;
      html += `<h${level}>${inlineMarkdown(heading[2])}</h${level}>`;
      continue;
    }

    if (/^[-*] /.test(line.trim())) {
      if (!listOpen) {
        html += '<ul>';
        listOpen = true;
      }
      html += `<li>${inlineMarkdown(line.trim().slice(2))}</li>`;
      continue;
    }

    if (/^>\s?/.test(line.trim())) {
      closeBlocks();
      html += `<blockquote><p>${inlineMarkdown(line.trim().replace(/^>\s?/, ''))}</p></blockquote>`;
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      closeBlocks();
      html += '<hr>';
      continue;
    }

    if (line.trim()) {
      closeBlocks();
      html += `<p>${inlineMarkdown(line)}</p>`;
    } else {
      closeBlocks();
    }
  }

  closeBlocks();
  if (codeOpen) {
    html += '</code></pre>';
  }

  return html;
}

function cleanTitle(title) {
  return String(title || '')
    .replace(/^Day\s*\d+\s*[-–—]\s*/i, '')
    .trim();
}

function extractTitle(markdown, fallback) {
  const match = String(markdown || '').match(/^#\s+(.+)$/m);
  return cleanTitle(match ? match[1] : fallback);
}

function extractDate(markdown) {
  const match = String(markdown || '').match(/\*\*Date:\*\*\s*(.+)$/m);
  return match ? match[1].trim() : '';
}

function extractOverview(markdown) {
  const overview = String(markdown || '').match(/## Overview\s+([\s\S]*?)(?=\n##|\n---|$)/i);
  if (overview && overview[1].trim()) {
    return overview[1].trim().replace(/\*\*/g, '').replace(/`/g, '');
  }
  const paragraph = String(markdown || '').split(/\r?\n/).find(line => line.trim() && !/^#/.test(line.trim()) && !/^Date:/i.test(line.trim()));
  return paragraph ? paragraph.trim().replace(/\*\*/g, '').replace(/`/g, '') : '';
}

function extractTags(markdown) {
  return [...String(markdown || '').matchAll(/^### \d+\.\s+(.+)$/gm)]
    .map(match => match[1].replace(/\*\*|`/g, '').replace(/\r/g, '').trim())
    .slice(0, 4);
}

function getFolderName(day) {
  return `DAY-${day}`;
}

function githubFolderUrl(folderName) {
  return `https://github.com/${REPO.owner}/${REPO.name}/tree/${REPO.branch}/${folderName}`;
}

function githubFileUrl(path) {
  return `${BLOB_ROOT}/${path}`;
}

function rawFileUrl(path) {
  return `${RAW_ROOT}/${path}`;
}

function isMarkdownFile(name) {
  return /\.md$/i.test(name);
}

function chooseMarkdownFile(files) {
  const preferredNames = ['readme.md', 'README.md', 'Readme.md', 'index.md', 'report.md'];
  const preferred = files.find(file => preferredNames.includes(file.name));
  if (preferred) {
    return preferred;
  }
  return files.find(file => isMarkdownFile(file.name)) || null;
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      Accept: 'application/vnd.github+json',
    },
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response.json();
}

async function fetchText(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response.text();
}

function buildReportsFromTree(tree = []) {
  const folders = new Map();

  for (const node of tree) {
    if (node.type !== 'blob') {
      continue;
    }

    const match = node.path.match(/^(DAY-(\d+))\/(.+)$/i);
    if (!match) {
      continue;
    }

    const folderName = match[1];
    const day = Number(match[2]);
    const fileName = match[3];

    if (!folders.has(day)) {
      folders.set(day, {
        day,
        folderName,
        folderUrl: githubFolderUrl(folderName),
        files: [],
      });
    }

    folders.get(day).files.push({
      name: fileName,
      path: node.path,
      url: githubFileUrl(node.path),
      rawUrl: rawFileUrl(node.path),
      isMarkdown: isMarkdownFile(fileName),
    });
  }

  return [...folders.values()].sort((left, right) => right.day - left.day);
}

async function hydrateReportsFromGithub() {
  const tree = await fetchJson(TREE_URL);
  const folders = buildReportsFromTree(tree.tree || []);

  const reports = await Promise.all(folders.map(async folder => {
    const markdownFile = chooseMarkdownFile(folder.files);
    const markdown = markdownFile ? await fetchText(markdownFile.rawUrl).catch(() => '') : '';
    const title = markdown ? extractTitle(markdown, folder.folderName) : folder.folderName;
    const date = markdown ? extractDate(markdown) : '';
    const overview = markdown ? extractOverview(markdown) : `Uploaded files inside ${folder.folderName}.`;
    const tags = markdown ? extractTags(markdown) : [];

    return {
      ...folder,
      markdown,
      markdownFile,
      title,
      date,
      overview,
      tags,
    };
  }));

  return reports;
}

function fallbackReports() {
  return FALLBACK_REPORTS.map(report => ({
    ...report,
    folderName: report.folderName || getFolderName(report.day),
    folderUrl: report.folderUrl || githubFolderUrl(getFolderName(report.day)),
    files: report.files || [],
    markdownFile: report.markdownFile || null,
    overview: report.overview || extractOverview(report.markdown || ''),
    tags: report.tags || extractTags(report.markdown || ''),
    date: report.date || extractDate(report.markdown || ''),
    title: report.title || getFolderName(report.day),
  }));
}

function renderFileList(files) {
  if (!files.length) {
    return '<p class="muted">No files were found in this folder yet.</p>';
  }

  return `
    <div class="file-grid">
      ${files.map(file => `
        <a class="file-chip" href="${file.url}" target="_blank" rel="noreferrer">
          <span>${escapeHtml(file.name)}</span>
          <small>${file.isMarkdown ? 'Markdown' : 'File'}</small>
        </a>
      `).join('')}
    </div>
  `;
}

function render(filter = '') {
  const query = filter.trim().toLowerCase();
  const reports = state.reports;
  const shown = reports.filter(report => {
    const haystack = [
      report.title,
      report.overview,
      report.date,
      report.folderName,
      ...(report.tags || []),
      ...(report.files || []).map(file => file.name),
      report.markdown || '',
    ].join(' ').toLowerCase();
    return haystack.includes(query);
  });

  const reportList = $('#report-list');
  const empty = $('#empty');
  const timeline = $('#timeline');

  timeline.innerHTML = reports.map(report => `
    <button class="timeline-btn" data-day="${report.day}">
      Day ${String(report.day).padStart(2, '0')} · ${report.date || report.folderName}
    </button>
  `).join('');

  reportList.innerHTML = shown.map(report => `
    <article class="report-card" data-day="${report.day}" tabindex="0">
      <span class="day-number">DAY ${String(report.day).padStart(2, '0')}</span>
      <div>
        <h3>${escapeHtml(cleanTitle(report.title))}</h3>
        <p>${escapeHtml(report.overview.slice(0, 210))}${report.overview.length > 210 ? '...' : ''}</p>
        <div class="tags">
          ${(report.tags || []).map(tag => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}
          <span class="tag">${report.files.length} file${report.files.length === 1 ? '' : 's'}</span>
        </div>
      </div>
      <div class="card-meta">
        ${escapeHtml(report.date || 'Uploaded on GitHub')}
        <span class="arrow">↗</span>
      </div>
    </article>
  `).join('');

  empty.hidden = shown.length > 0;
  empty.textContent = state.loading
    ? 'Loading reports from GitHub...'
    : 'No notes found. Try another search.';

  document.querySelectorAll('.report-card').forEach(card => {
    const open = () => showReport(Number(card.dataset.day));
    card.onclick = open;
    card.onkeydown = event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        open();
      }
    };
  });

  document.querySelectorAll('.timeline-btn').forEach(button => {
    button.onclick = () => showReport(Number(button.dataset.day));
  });

  $('#day-count').textContent = String(reports.length).padStart(2, '0');
  $('#topic-count').textContent = String(new Set(reports.flatMap(report => report.tags || [])).size || reports.reduce((count, report) => count + report.files.length, 0) || 0);
  $('#last-updated').textContent = state.loading
    ? 'Loading from GitHub...'
    : state.source === 'GitHub'
      ? 'Live from GitHub'
      : 'Showing cached reports';
}

function showReport(day) {
  const report = state.reports.find(entry => entry.day === day);
  if (!report) {
    return;
  }

  $('#reader-content').innerHTML = `
    ${report.markdown ? markdownToHtml(report.markdown) : `<h1>${escapeHtml(report.folderName)}</h1><p>${escapeHtml(report.overview)}</p>`}
    <h2>Files in this folder</h2>
    ${renderFileList(report.files)}
    <p><a class="button primary" target="_blank" rel="noreferrer" href="${report.folderUrl}">Open folder on GitHub ↗</a></p>
  `;

  $('#reader').showModal();
}

async function loadReports() {
  state.loading = true;
  state.reports = fallbackReports();
  render();

  try {
    state.reports = await hydrateReportsFromGithub();
    state.source = 'GitHub';
  } catch (error) {
    state.reports = fallbackReports();
    state.source = 'fallback';
    console.warn('Using fallback reports because live GitHub fetch failed:', error);
  } finally {
    state.loading = false;
    render(state.filter);
  }
}

$('#search').oninput = event => {
  state.filter = event.target.value;
  render(state.filter);
};

$('.close').onclick = () => $('#reader').close();
$('#reader').onclick = event => {
  if (event.target === $('#reader')) {
    $('#reader').close();
  }
};

loadReports();
