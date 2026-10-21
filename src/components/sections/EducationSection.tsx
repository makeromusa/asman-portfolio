import { educationList } from "@/data/education";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { GraduationCap, Award, Calendar } from "lucide-react";

export function EducationSection() {
  return (
    <section id="education" className="py-20 px-4 sm:px-6 lg:px-8 bg-slate-50/50 dark:bg-slate-900/20 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-4xl mx-auto">
        <SectionHeading
          badge="Background"
          title="Education & Certifications"
          subtitle="Academic degree, computer science fundamentals, and continuous professional skill development."
        />

        <div className="space-y-6">
          {educationList.map((item) => (
            <div
              key={item.id}
              className="p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 shadow-sm"
            >
              <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-3">
                <div className="flex items-start gap-4">
                  <div className="p-2.5 rounded-xl bg-blue-100 dark:bg-blue-950/80 text-blue-600 dark:text-blue-400 shrink-0">
                    {item.type === "degree" ? (
                      <GraduationCap className="w-6 h-6" />
                    ) : (
                      <Award className="w-6 h-6" />
                    )}
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-slate-900 dark:text-white">
                      {item.title}
                    </h3>
                    <p className="text-sm font-semibold text-blue-600 dark:text-blue-400 mt-0.5">
                      {item.institution}
                    </p>
                  </div>
                </div>

                <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 shrink-0 self-start">
                  <Calendar className="w-3.5 h-3.5" />
                  <span>
                    {item.startDate} {item.endDate ? `– ${item.endDate}` : "– Present"}
                  </span>
                </div>
              </div>

              {item.description && (
                <p className="mt-4 text-sm text-slate-600 dark:text-slate-400 leading-relaxed sm:pl-14">
                  {item.description}
                </p>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
