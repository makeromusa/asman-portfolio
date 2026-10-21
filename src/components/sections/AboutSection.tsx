import { siteConfig } from "@/data/siteConfig";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { CheckCircle2, Cpu, Database, Globe } from "lucide-react";

export function AboutSection() {
  const highlights = [
    {
      icon: Globe,
      title: "Full-Stack Web Engineering",
      desc: "Architecting responsive, modern web apps with Next.js, React, and TypeScript.",
    },
    {
      icon: Database,
      title: "Data Persistence & APIs",
      desc: "Designing relational schemas with PostgreSQL/Supabase and flexible NoSQL with MongoDB.",
    },
    {
      icon: Cpu,
      title: "Algorithmic Problem Solving",
      desc: "Strong computer science fundamentals rooted in C/C++, Java, and Python.",
    },
  ];

  return (
    <section id="about" className="py-20 px-4 sm:px-6 lg:px-8 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-5xl mx-auto">
        <SectionHeading
          badge="Background"
          title="About Me"
          subtitle="Engineering robust digital experiences with modern tools and clean architecture."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          {/* Bio text */}
          <div className="lg:col-span-7 space-y-5 text-slate-600 dark:text-slate-300 text-base leading-relaxed">
            <p>{siteConfig.bio}</p>
            <p>
              I take pride in following structured engineering workflows — from thorough requirements analysis and modular architecture design, to rigorous testing and automated continuous deployment.
            </p>
            <p>
              When not writing code, I actively explore emerging cloud services, contribute to collaborative development, and refine my understanding of distributed systems and scalable web standards.
            </p>

            <div className="pt-2 flex flex-wrap gap-4 text-sm font-medium text-slate-800 dark:text-slate-200">
              <span className="inline-flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                Clean Code Standards
              </span>
              <span className="inline-flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                Modern Next.js & TypeScript
              </span>
              <span className="inline-flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                Cloud & CI/CD Driven
              </span>
            </div>
          </div>

          {/* Key Engineering Pillars Cards */}
          <div className="lg:col-span-5 space-y-4">
            {highlights.map((item, idx) => {
              const Icon = item.icon;
              return (
                <div
                  key={idx}
                  className="p-5 rounded-2xl border border-slate-200 dark:border-slate-800/80 bg-white/60 dark:bg-slate-900/40 backdrop-blur-sm shadow-sm hover:border-blue-500/50 dark:hover:border-blue-500/50 transition-all duration-200"
                >
                  <div className="flex items-start gap-4">
                    <div className="p-2.5 rounded-xl bg-blue-100 dark:bg-blue-950/80 text-blue-600 dark:text-blue-400 shrink-0">
                      <Icon className="w-5 h-5" />
                    </div>
                    <div>
                      <h4 className="text-base font-bold text-slate-900 dark:text-white">
                        {item.title}
                      </h4>
                      <p className="mt-1 text-xs sm:text-sm text-slate-500 dark:text-slate-400">
                        {item.desc}
                      </p>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
