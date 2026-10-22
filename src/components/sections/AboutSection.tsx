import { siteConfig } from "@/data/siteConfig";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { CheckCircle2, Cpu, Database, Globe, MapPin, GraduationCap } from "lucide-react";

export function AboutSection() {
  const highlights = [
    {
      icon: Cpu,
      title: "Agentic AI & LLM Systems",
      desc: "Architecting multi-agent pipelines, prompt constraints, and cloud-native AI integration with Amazon Bedrock.",
    },
    {
      icon: Globe,
      title: "Full-Stack Web Engineering",
      desc: "Building high-performance, modern web applications with Next.js 15, TypeScript, and Tailwind CSS.",
    },
    {
      icon: Database,
      title: "Relational Data Architectures",
      desc: "3NF database modeling, SQL Server, Oracle Database/APEX, and automated documentation pipelines.",
    },
  ];

  return (
    <section id="about" className="py-20 px-4 sm:px-6 lg:px-8 border-t border-slate-200/60 dark:border-slate-800/60">
      <div className="max-w-6xl mx-auto">
        <SectionHeading
          badge="Background"
          title="About Me"
          subtitle="Engineering robust digital systems, agentic AI workflows, and scalable software architectures."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          {/* Portrait Image Card */}
          <div className="lg:col-span-5 flex justify-center">
            <div className="relative group max-w-sm w-full">
              <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-3xl blur opacity-25 group-hover:opacity-40 transition duration-300" />
              <div className="relative rounded-3xl overflow-hidden border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-xl">
                <img
                  src="/images/asman-full.jpg"
                  alt={siteConfig.name}
                  className="w-full h-auto object-cover object-top max-h-[460px]"
                />
                <div className="p-5 bg-white/95 dark:bg-slate-900/95 backdrop-blur-sm border-t border-slate-100 dark:border-slate-800">
                  <h3 className="font-bold text-lg text-slate-900 dark:text-white">{siteConfig.name}</h3>
                  <div className="mt-2 space-y-1.5 text-xs text-slate-600 dark:text-slate-300">
                    <p className="flex items-center gap-1.5">
                      <GraduationCap className="w-4 h-4 text-blue-600 dark:text-blue-400 shrink-0" />
                      <span>B.Sc. Computer Science • University of Nairobi</span>
                    </p>
                    <p className="flex items-center gap-1.5">
                      <MapPin className="w-4 h-4 text-blue-600 dark:text-blue-400 shrink-0" />
                      <span>Nairobi, Kenya</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Bio text & Highlights */}
          <div className="lg:col-span-7 space-y-6">
            <div className="space-y-4 text-slate-600 dark:text-slate-300 text-base leading-relaxed">
              <p>{siteConfig.bio}</p>
              <p>
                From low-level systems programming in C/C++ to autonomous multi-agent frameworks and enterprise web applications, I adhere to strict SDLC standards, clean design patterns, and continuous deployment.
              </p>

              <div className="pt-2 flex flex-wrap gap-4 text-sm font-medium text-slate-800 dark:text-slate-200">
                <span className="inline-flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                  Systems &amp; Low-Level (C/C++)
                </span>
                <span className="inline-flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                  Multi-Agent &amp; LLM Systems
                </span>
                <span className="inline-flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                  Full-Stack Next.js 15
                </span>
              </div>
            </div>

            {/* Key Engineering Pillars Cards */}
            <div className="space-y-3 pt-2">
              {highlights.map((item, idx) => {
                const Icon = item.icon;
                return (
                  <div
                    key={idx}
                    className="p-4 rounded-xl border border-slate-200 dark:border-slate-800/80 bg-white/60 dark:bg-slate-900/40 backdrop-blur-sm shadow-sm hover:border-blue-500/50 dark:hover:border-blue-500/50 transition-all duration-200"
                  >
                    <div className="flex items-start gap-3.5">
                      <div className="p-2 rounded-lg bg-blue-100 dark:bg-blue-950/80 text-blue-600 dark:text-blue-400 shrink-0">
                        <Icon className="w-4 h-4" />
                      </div>
                      <div>
                        <h4 className="text-sm font-bold text-slate-900 dark:text-white">
                          {item.title}
                        </h4>
                        <p className="mt-0.5 text-xs text-slate-500 dark:text-slate-400">
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
      </div>
    </section>
  );
}
