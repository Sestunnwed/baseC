# 获取 PR 的修改文件
modified_files = git.modified_files + git.added_files

# 生成 PR 摘要
summary = "### 🤖 PR 自动摘要\n"
summary += "- 影响的文件数量：#{modified_files.count}\n"
summary += "- 主要修改文件：\n"

modified_files.first(5).each do |file|
  summary += "  - `#{file}`\n"
end

# 在 PR 页面评论这个摘要
message(summary)
