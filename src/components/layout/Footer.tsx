import { siteConfig } from "@/data/siteConfig";
import { SocialLinks } from "@/components/ui/SocialLinks";

export function Footer() {
  const currentYear = 2026;

  return (
    <footer className="border-t border-slate-200 dark:border-slate-800/80 bg-white dark:bg-slate-950 py-12 transition-colors">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="text-center md:text-left">
            <p className="text-sm font-semibold text-slate-900 dark:text-white">
              {siteConfig.name} — {siteConfig.title}
            </p>
            <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">
              © {currentYear} All rights reserved. Built with Next.js, TypeScript & Tailwind CSS.
            </p>
          </div>

          <SocialLinks iconClassName="w-4 h-4" />
        </div>
      </div>
    </footer>
  );
}
