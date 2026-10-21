import Link from "next/link";
import { getAllPosts } from "@/lib/blog";
import { BlogPostCard } from "@/components/ui/BlogPostCard";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { ArrowRight, BookOpen } from "lucide-react";

export function BlogPreviewSection() {
  const posts = getAllPosts().slice(0, 3);

  if (posts.length === 0) return null;

  return (
    <section id="blog" className="py-20 px-4 sm:px-6 lg:px-8 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-6xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
          <SectionHeading
            badge="Writing & Insights"
            title="Technical Articles & Thought Leadership"
            subtitle="Deep dives into software engineering, architectural trade-offs, and full-stack development."
          />

          <Link
            href="/blog"
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/50 border border-blue-200 dark:border-blue-900/60 hover:bg-blue-100 dark:hover:bg-blue-900/40 transition-colors shrink-0 self-start md:self-auto mb-12 md:mb-0"
          >
            <BookOpen className="w-4 h-4" />
            <span>View All Articles</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {posts.map((post) => (
            <BlogPostCard key={post.slug} post={post} />
          ))}
        </div>
      </div>
    </section>
  );
}
