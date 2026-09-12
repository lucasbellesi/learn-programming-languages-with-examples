import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import { Account } from "@/components/account";
import { ThemeButton, ThemeProvider } from "@/components/theme";
export const metadata: Metadata = {
    title: { default: "Code by Example", template: "%s · Code by Example" },
    description:
        "Learn six programming languages through examples, guided practice, and clear feedback.",
};
export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en" data-scroll-behavior="smooth" suppressHydrationWarning>
            <head>
                <script
                    dangerouslySetInnerHTML={{
                        __html: `try{var t=localStorage.getItem('code-by-example-theme');document.documentElement.dataset.theme=(t==='light'||t==='dark')?t:(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}catch{}`,
                    }}
                />
            </head>
            <body>
                <ThemeProvider>
                    <a className="skip" href="#main">
                        Skip to content
                    </a>
                    <header className="header">
                        <Link className="brand" href="/">
                            <span className="logo">{"{ }"}</span> code
                            <span className="muted">by</span>example
                        </Link>
                        <nav>
                            <Link href="/">Explore the curriculum</Link>
                            <ThemeButton />
                            <Account />
                        </nav>
                    </header>
                    {children}
                    <footer>
                        Built for curiosity. Learn one concept, then see it in
                        six languages.
                        <a href="https://github.com/lucasbellesi/learn-programming-languages-with-examples">
                            View the curriculum on GitHub ↗
                        </a>
                    </footer>
                </ThemeProvider>
            </body>
        </html>
    );
}
