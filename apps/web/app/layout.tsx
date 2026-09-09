import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import { Account } from "@/components/account";
export const metadata: Metadata = {
    title: { default: "Code by Example", template: "%s · Code by Example" },
    description:
        "Learn six programming languages through examples, guided practice, and clear feedback.",
};
export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en" data-scroll-behavior="smooth">
            <body>
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
                        <Account />
                    </nav>
                </header>
                {children}
                <footer>
                    Built for curiosity. Learn one concept, then see it in six
                    languages.
                    <a href="https://github.com/lucasbellesi/learn-programming-languages-with-examples">
                        View the curriculum on GitHub ↗
                    </a>
                </footer>
            </body>
        </html>
    );
}
