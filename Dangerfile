# 获取 Git 变更信息
modified_files = git.modified_files
added_files = git.added_files
deleted_files = git.deleted_files

# 统计代码变更行数
insertions = git.lines_of_code[:insertions]
deletions = git.lines_of_code[:deletions]
total_lines_changed = git.lines_of_code


# 获取 PR 元数据
pr_title = github.pull_request.title  # 获取 PR 标题
pr_labels = github.pull_request.labels.map(&:name).join(", ")  # 获取 PR 标签
pr_reviewers = github.pull_request.requested_reviewers.map { |r| r["login"] }.join(", ")  # 获取请求的 reviewers

# 获取提交信息
commit_messages = github.commits.map(&:message).join("\n- ")

# 读取 PR 描述（如果为空，则生成默认摘要）
pr_body = github.pr_body.strip
pr_body = "ℹ️ 此 PR 没有描述，自动生成摘要：" if pr_body.empty?

# **分析 PR 类型**
summary_text = []
if added_files.any?
  summary_text << "📂 新增了 #{added_files.count} 个文件，可能是新功能或配置更新。"
end

# **分析涉及的模块**
module_summary = []
module_mapping = {
  "src/network" => "🌐 网络模块",
  "src/db" => "🗄️ 数据库模块",
  "src/ui" => "🎨 前端 UI",
  "public" => "🎨 设计资源",
  "assets" => "🖼️ 图片/图标",
  "styles" => "🎨 样式文件（CSS/SCSS）",
  "config" => "⚙️ 配置文件",
  "tests" => "🧪 测试代码",
  "scripts" => "🔧 脚本工具",
  "docs" => "📖 文档",
  "github" => "🔑 GitHub 元数据"  # GitHub 元数据模块
}
modified_files.each do |file|
  module_mapping.each do |path, module_name|
    if file.start_with?(path)
      module_summary << module_name unless module_summary.include?(module_name)
    end
  end
end

# **生成 PR 摘要**
summary = <<~MD
  ### 🤖 PR 自动总结
  📌 **PR 标题**：
  - #{pr_title}

  📌 **变更类型**：
  - #{summary_text.join("\n- ")}

  📊 **代码变更统计**：
  - 影响文件数量：#{modified_files.count + added_files.count + deleted_files.count}
  - 代码变更行数：#{total_lines_changed}

  🔍 **涉及的模块**：
  #{module_summary.any? ? module_summary.join(", ") : "⚠️ 无法确定，可能涉及多个模块"}

  🔑 **PR 元数据**：
  - **标签**：#{pr_labels.empty? ? "无" : pr_labels}
  - **请求的 Reviewers**：#{pr_reviewers.empty? ? "无" : pr_reviewers}

  ✏️ **主要修改的文件**：
  #{modified_files.first(5).map { |file| "  - `#{file}`" }.join("\n")}

  📝 **最近的 Commit 信息**：
  - #{commit_messages}
MD

# **在 PR 页面发表评论**
message(summary)
