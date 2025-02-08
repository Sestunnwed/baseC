# 获取 PR 的修改文件
modified_files = git.modified_files + git.added_files
deleted_files = git.deleted_files

# 计算 PR 修改的行数
total_lines_changed = git.lines_of_code

# 生成 PR 摘要
summary = "### 🤖 PR 自动摘要\n"
summary += "- 影响的文件数量：#{modified_files.count + deleted_files.count}\n"
summary += "- 新增文件：#{git.added_files.count}\n"
summary += "- 修改文件：#{git.modified_files.count}\n"
summary += "- 删除文件：#{git.deleted_files.count}\n"
summary += "- 代码变更总行数：#{total_lines_changed}\n"
summary += "- 主要修改文件：\n"

modified_files.first(5).each do |file|
  summary += "  - `#{file}`\n"
end

# 如果有删除的文件，也展示前 5 个
unless deleted_files.empty?
  summary += "- 主要删除文件：\n"
  deleted_files.first(5).each do |file|
    summary += "  - `#{file}`\n"
  end
end

# 自动检查 PR 描述是否填写完整
if github.pr_body.nil? || github.pr_body.strip.empty?
  warn("PR 描述为空，请补充详细的修改说明。")
end

target_branch = github.branch_for_base
# 如果目标分支是 main 或 master，则发出警告
if target_branch == "main" || target_branch == "master"
  warn("PR 目标分支为 `#{target_branch}`，请确保此 PR 符合合并策略！")
end

# 在 PR 页面评论这个摘要
markdown(summary)
