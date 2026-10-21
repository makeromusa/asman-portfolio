import { skills } from "@/data/skills";
import { SkillCategory } from "@/types";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { Code, Layout, Server, Database, Wrench } from "lucide-react";

export function SkillsSection() {
  const categories: { name: SkillCategory; icon: typeof Code }[] = [
    { name: "Languages", icon: Code },
    { name: "Frontend", icon: Layout },
    { name: "Backend", icon: Server },
    { name: "Database", icon: Database },
    { name: "Tools & DevOps", icon: Wrench },
  ];

  return (
    <section id="skills" className="py-20 px-4 sm:px-6 lg:px-8 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-6xl mx-auto">
        <SectionHeading
          badge="Expertise"
          title="Skills & Technologies"
          subtitle="My technical repertoire across core programming languages, modern frameworks, database engines, and developer tooling."
        />

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {categories.map(({ name, icon: Icon }) => {
            const categorySkills = skills.filter((s) => s.category === name);
            if (categorySkills.length === 0) return null;

            return (
              <div
                key={name}
                className="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/40 backdrop-blur-sm shadow-sm"
              >
                <div className="flex items-center gap-3 mb-5">
                  <div className="p-2.5 rounded-xl bg-blue-100 dark:bg-blue-950/80 text-blue-600 dark:text-blue-400">
                    <Icon className="w-5 h-5" />
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                    {name}
                  </h3>
                </div>

                <div className="flex flex-wrap gap-2">
                  {categorySkills.map((skill) => (
                    <span
                      key={skill.name}
                      className="px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-100 dark:bg-slate-800/90 text-slate-700 dark:text-slate-300 border border-slate-200/60 dark:border-slate-700/60 hover:border-blue-500/50 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                    >
                      {skill.name}
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
