"use client";

import { siteConfig } from "@/data/siteConfig";
import { SocialLinks } from "@/components/ui/SocialLinks";
import { ArrowRight, Download, Terminal } from "lucide-react";

export function HeroSection() {
  return (
    <section className="relative min-h-[calc(100vh-4rem)] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden">
      {/* Background Glow Accents */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-blue-500/10 dark:bg-blue-600/15 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-72 h-72 bg-indigo-500/10 dark:bg-indigo-600/15 rounded-full blur-3xl pointer-events-none" />

      <div className="relative max-w-4xl mx-auto text-center z-10">
        {/* Status / Role pill */}
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-900/60 text-blue-700 dark:text-blue-300 text-xs sm:text-sm font-medium mb-8">
          <Terminal className="w-4 h-4 text-blue-600 dark:text-blue-400" />
          <span>Available for New Roles & Engineering Projects</span>
        </div>

        {/* Main Title & Headline */}
        <h1 className="text-4xl sm:text-6xl md:text-7xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-6">
          Hi, I&apos;m{" "}
          <span className="bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-300 bg-clip-text text-transparent">
            {siteConfig.name}
          </span>
        </h1>

        <p className="text-xl sm:text-2xl font-semibold text-slate-700 dark:text-slate-300 mb-4">
          {siteConfig.title}
        </p>

        <p className="max-w-2xl mx-auto text-base sm:text-lg text-slate-600 dark:text-slate-400 mb-10 leading-relaxed">
          {siteConfig.tagline}
        </p>

        {/* Action Buttons */}
        <div className="flex flex-wrap items-center justify-center gap-4 mb-12">
          <a
            href="#projects"
            className="inline-flex items-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-white bg-blue-600 hover:bg-blue-700 transition-all shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/30"
          >
            <span>Explore Projects</span>
            <ArrowRight className="w-4 h-4" />
          </a>
          <a
            href={siteConfig.resumeUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-slate-800 dark:text-slate-200 bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all shadow-sm"
          >
            <Download className="w-4 h-4" />
            <span>Download CV</span>
          </a>
        </div>

        {/* Social Links */}
        <div className="flex justify-center">
          <SocialLinks />
        </div>
      </div>
    </section>
  );
}
