import { testimonials } from "@/data/testimonials";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { Quote } from "lucide-react";

export function TestimonialsSection() {
  return (
    <section id="testimonials" className="py-20 px-4 sm:px-6 lg:px-8 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-5xl mx-auto">
        <SectionHeading
          badge="Endorsements"
          title="Testimonials & Peer Reviews"
          subtitle="What fellow developers, project collaborators, and mentors have shared about working together."
        />

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {testimonials.map((t) => (
            <div
              key={t.id}
              className="flex flex-col justify-between p-8 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/40 shadow-sm relative"
            >
              <Quote className="w-8 h-8 text-blue-500/20 dark:text-blue-400/20 mb-4" />
              <p className="text-slate-600 dark:text-slate-300 text-sm sm:text-base leading-relaxed italic">
                &ldquo;{t.quote}&rdquo;
              </p>

              <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800/80 flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white font-bold text-sm">
                  {t.name.charAt(0)}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-white">
                    {t.name}
                  </h4>
                  <p className="text-xs text-slate-500 dark:text-slate-400">
                    {t.role} {t.company ? `• ${t.company}` : ""}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
