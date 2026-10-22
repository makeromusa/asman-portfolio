import { Skill } from "@/types";

export const skills: Skill[] = [
  // Languages
  { name: "Python", category: "Languages" },
  { name: "C / C++", category: "Languages" },
  { name: "TypeScript", category: "Languages" },
  { name: "JavaScript", category: "Languages" },
  { name: "SQL (Oracle, SQL Server)", category: "Languages" },
  { name: "Java", category: "Languages" },

  // AI & Systems (Grouped under Tools & DevOps / Backend)
  { name: "Prompt Engineering", category: "Tools & DevOps" },
  { name: "LLM Benchmarking & Eval", category: "Tools & DevOps" },
  { name: "Multi-Agent Systems", category: "Backend" },
  { name: "Amazon Bedrock", category: "Backend" },
  { name: "Google Gemini AI", category: "Backend" },
  { name: "RLHF & Model Output Eval", category: "Tools & DevOps" },

  // Frontend
  { name: "Next.js", category: "Frontend" },
  { name: "React", category: "Frontend" },
  { name: "Tailwind CSS", category: "Frontend" },
  { name: "HTML5 / CSS3", category: "Frontend" },
  { name: "Streamlit", category: "Frontend" },

  // Backend
  { name: "Node.js", category: "Backend" },
  { name: "REST APIs", category: "Backend" },
  { name: "Automated Tech Docs", category: "Backend" },

  // Database
  { name: "PostgreSQL", category: "Database" },
  { name: "Oracle Database & APEX", category: "Database" },
  { name: "SQL Server (SSMS)", category: "Database" },
  { name: "Supabase", category: "Database" },
  { name: "Power BI & Excel Modeling", category: "Database" },

  // Tools & DevOps
  { name: "Linux (Red Hat)", category: "Tools & DevOps" },
  { name: "Git & GitHub", category: "Tools & DevOps" },
  { name: "Vercel", category: "Tools & DevOps" },
  { name: "Zapier Automation", category: "Tools & DevOps" },
];
