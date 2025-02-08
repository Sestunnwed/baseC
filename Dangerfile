# 获取 Git 变更信息
modified_files = git.modified_files
added_files = git.added_files
deleted_files = git.deleted_files

# 统计代码变更行数
insertions = git.lines_of_code[:insertions]
deletions = git.lines_of_code[:deletions]

# 获取 PR 提交信息
commit_messages = github.commits.map(&:message).join("\n- ")

# 读取 PR 说明（如果为空，则生成默认摘要）
pr_body = github.pr_body.strip
pr_body = "ℹ️ 此 PR 没有描述，自动生成摘要：" if pr_body.empty?

# **分析 PR 类型**
summary_text = []
if added_files.any?
  summary_text << "📂 新增了 #{added_files.count} 个文件，可能是新功能或配置更新。"
end
if deleted_files.any?
  summary_text << "🗑️ 删除了 #{deleted_files.count} 个文件，可能是重构或移除无用代码。"
end
if insertions > deletions
  summary_text << "📈 本次 PR 主要增加了代码（+#{insertions} 行），可能是新功能开发。"
elsif deletions > insertions
  summary_text << "📉 本次 PR 主要删除了代码（-#{deletions} 行），可能是优化或精简。"
else
  summary_text << "⚡ 代码改动较小，可能是修复或格式调整。"
end

# **分析涉及的模块**
module_summary = []
module_mapping = {
  "./github/workflows" => "📃 github模块",
  "src/network" => "🌐 网络模块",
  "src/db" => "🗄️ 数据库模块",
  "src/ui" => "🎨 前端 UI",
  "public" => "🎨 设计资源",
  "assets" => "🖼️ 图片/图标",
  "styles" => "🎨 样式文件（CSS/SCSS）",
  "config" => "⚙️ 配置文件",
  "tests" => "🧪 测试代码",
  "scripts" => "🔧 脚本工具",
  "docs" => "📖 文档"
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
  📌 **变更类型**：
  - #{summary_text.join("\n- ")}

  📊 **代码变更统计**：
  - 影响文件数量：#{modified_files.count + added_files.count + deleted_files.count}
  - 代码变更行数：+#{insertions} / -#{deletions}

  🔍 **涉及的模块**：
  #{module_summary.any? ? module_summary.join(", ") : "⚠️ 无法确定，可能涉及多个模块"}

  ✏️ **主要修改的文件**：
  #{modified_files.first(5).map { |file| "  - `#{file}`" }.join("\n")}

  📝 **最近的 Commit 信息**：
  - #{commit_messages}
MD

# **在 PR 页面发表评论**
message(summary)
