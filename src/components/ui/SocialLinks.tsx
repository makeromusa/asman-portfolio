import { siteConfig } from "@/data/siteConfig";
import { GithubIcon, LinkedinIcon, TwitterXIcon } from "./Icons";
import { Mail } from "lucide-react";

interface SocialLinksProps {
  className?: string;
  iconClassName?: string;
}

export function SocialLinks({ className = "", iconClassName = "w-5 h-5" }: SocialLinksProps) {
  const { socials } = siteConfig;

  const links = [
    { label: "GitHub", href: socials.github, icon: GithubIcon },
    { label: "LinkedIn", href: socials.linkedin, icon: LinkedinIcon },
    { label: "Twitter", href: socials.twitter, icon: TwitterXIcon },
    { label: "Email", href: `mailto:${socials.email}`, icon: Mail },
  ].filter((item) => Boolean(item.href));

  return (
    <div className={`flex items-center gap-3 ${className}`}>
      {links.map(({ label, href, icon: Icon }) => (
        <a
          key={label}
          href={href}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={label}
          className="p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white/50 dark:bg-slate-900/50 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 transition-all duration-200 shadow-sm"
        >
          <Icon className={iconClassName} />
        </a>
      ))}
    </div>
  );
}
