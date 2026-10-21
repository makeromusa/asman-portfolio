import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { BlogPost } from "@/types";

const postsDirectory = path.join(process.cwd(), "src/content/blog");

export function getAllPosts(): BlogPost[] {
  if (!fs.existsSync(postsDirectory)) {
    return [];
  }

  const fileNames = fs.readdirSync(postsDirectory);
  const allPosts = fileNames
    .filter((fileName) => fileName.endsWith(".md") || fileName.endsWith(".mdx"))
    .map((fileName) => {
      const slug = fileName.replace(/\.(md|mdx)$/, "");
      const fullPath = path.join(postsDirectory, fileName);
      const fileContents = fs.readFileSync(fullPath, "utf8");
      const { data, content } = matter(fileContents);

      // Estimate reading time (~200 words per minute)
      const wordCount = content.split(/\s+/g).length;
      const readingTime = `${Math.max(1, Math.ceil(wordCount / 200))} min read`;

      return {
        slug,
        title: data.title || "Untitled Post",
        excerpt: data.excerpt || "",
        date: data.date || "2026-10-21",
        readingTime,
        tags: data.tags || ["Engineering"],
        published: data.published !== false,
        coverImage: data.coverImage,
      } as BlogPost;
    })
    .filter((post) => post.published)
    .sort((a, b) => (new Date(b.date).getTime() - new Date(a.date).getTime()));

  return allPosts;
}

export function getPostBySlug(slug: string): { post: BlogPost; content: string } | null {
  const fullPathMd = path.join(postsDirectory, `${slug}.md`);
  const fullPathMdx = path.join(postsDirectory, `${slug}.mdx`);

  let targetPath = "";
  if (fs.existsSync(fullPathMd)) {
    targetPath = fullPathMd;
  } else if (fs.existsSync(fullPathMdx)) {
    targetPath = fullPathMdx;
  } else {
    return null;
  }

  const fileContents = fs.readFileSync(targetPath, "utf8");
  const { data, content } = matter(fileContents);

  const wordCount = content.split(/\s+/g).length;
  const readingTime = `${Math.max(1, Math.ceil(wordCount / 200))} min read`;

  const post: BlogPost = {
    slug,
    title: data.title || "Untitled Post",
    excerpt: data.excerpt || "",
    date: data.date || "2026-10-21",
    readingTime,
    tags: data.tags || ["Engineering"],
    published: data.published !== false,
    coverImage: data.coverImage,
  };

  return { post, content };
}
