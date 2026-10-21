import { Project } from "@/types";
import { ExternalLink, FolderGit2 } from "lucide-react";
import { GithubIcon } from "./Icons";

interface ProjectCardProps {
  project: Project;
}

export function ProjectCard({ project }: ProjectCardProps) {
  return (
    <div className="group flex flex-col rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 overflow-hidden shadow-sm hover:shadow-md hover:border-blue-500/50 dark:hover:border-blue-500/50 transition-all duration-300">
      {/* Visual Header / Placeholder Thumbnail */}
      <div className="relative h-48 w-full bg-gradient-to-br from-slate-100 to-slate-200 dark:from-slate-800/80 dark:to-slate-900/80 flex items-center justify-center p-6 border-b border-slate-200 dark:border-slate-800">
        <FolderGit2 className="w-12 h-12 text-slate-400 dark:text-slate-600 group-hover:scale-110 group-hover:text-blue-500 transition-all duration-300" />
        <span className="absolute top-3 right-3 px-2.5 py-1 text-xs font-semibold rounded-full bg-white/80 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 backdrop-blur-sm">
          {project.category}
        </span>
      </div>

      {/* Card Content */}
      <div className="flex-1 p-6 flex flex-col justify-between">
        <div>
          <h3 className="text-xl font-bold text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
            {project.title}
          </h3>
          <p className="mt-2.5 text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
            {project.description}
          </p>
        </div>

        {/* Tech Stack Pills & Links */}
        <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800/80">
          <div className="flex flex-wrap gap-1.5 mb-5">
            {project.technologies.map((tech) => (
              <span
                key={tech}
                className="px-2.5 py-0.5 text-xs font-medium rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300"
              >
                {tech}
              </span>
            ))}
          </div>

          <div className="flex items-center gap-3">
            {project.githubUrl && (
              <a
                href={project.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="GitHub repository"
                className="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
              >
                <GithubIcon className="w-4 h-4" />
                <span>Source</span>
              </a>
            )}
            {project.liveUrl && project.liveUrl !== "#" && (
              <a
                href={project.liveUrl}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Live preview"
                className="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors ml-auto"
              >
                <span>Live Demo</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
