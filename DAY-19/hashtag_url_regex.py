import re
# 8. Extract Hashtags
text = "Learning #python and #agenticai with #auribises"

hashtags = re.findall(r"#\w+", text)

print("8. Hashtags")
print(hashtags)


# 9. Extract URLs
text = "Visit https://finlo.in to learn Python."

urls = re.findall(r"https?://\S+", text)

print("\n9. URLs")
print(urls)
