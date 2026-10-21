export type ProjectCategory = 'Full-Stack' | 'Frontend' | 'Backend' | 'Mobile' | 'AI' | 'Other';

export interface Project {
  id: string;
  title: string;
  description: string;
  longDescription?: string;
  technologies: string[];
  category: ProjectCategory;
  liveUrl?: string;
  githubUrl?: string;
  imageUrl: string;
  featured: boolean;
  date: string;
}

export type SkillCategory = 'Languages' | 'Frontend' | 'Backend' | 'Database' | 'Tools & DevOps';

export interface Skill {
  name: string;
  category: SkillCategory;
  icon?: string;
}

export interface EducationItem {
  id: string;
  type: 'degree' | 'certification';
  title: string;
  institution: string;
  startDate: string;
  endDate?: string;
  description?: string;
  url?: string;
}

export interface Testimonial {
  id: string;
  quote: string;
  name: string;
  role: string;
  company?: string;
  avatarUrl?: string;
}

export interface BlogPost {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readingTime: string;
  tags: string[];
  published: boolean;
  coverImage?: string;
}

export interface ContactSubmission {
  name: string;
  email: string;
  subject: string;
  message: string;
  timestamp: string;
}

export interface SocialLinks {
  github: string;
  linkedin: string;
  twitter?: string;
  email: string;
}

export interface SiteConfig {
  name: string;
  title: string;
  tagline: string;
  bio: string;
  avatar: string;
  socials: SocialLinks;
  resumeUrl: string;
}
