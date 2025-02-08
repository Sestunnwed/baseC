# 获取 PR 变更信息
modified_files = git.modified_files
added_files = git.added_files
deleted_files = git.deleted_files

# 统计变更行数
insertions = git.lines_of_code[:insertions]
deletions = git.lines_of_code[:deletions]

# 获取提交信息
commit_messages = github.commits.map(&:message).join("\n- ")

# 获取 PR 说明（如果为空，则生成一个）
pr_body = github.pr_body
pr_body = "ℹ️ 此 PR 没有描述，自动生成摘要：" if pr_body.strip.empty?

# 生成 PR 摘要
summary = <<~MD
  ### 🤖 PR 自动摘要
  📌 **影响的文件数量**：#{modified_files.count + added_files.count + deleted_files.count}
  ➕ **新增文件**: #{added_files.any? ? added_files.join(", ") : "无"}
  ✏️ **修改文件**: #{modified_files.any? ? modified_files.join(", ") : "无"}
  ❌ **删除文件**: #{deleted_files.any? ? deleted_files.join(", ") : "无"}
  📊 **代码变更行数**：+#{insertions} / -#{deletions}

  ### 🔍 变更详情
  #{pr_body}

  ### 📝 最近的 Commit 信息
  - #{commit_messages}
MD

# 在 PR 页面发表评论
message(summary)
