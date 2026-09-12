import { catalog } from "@/lib/catalog";
import { Explorer } from "@/components/explorer";
export default function Home() {
    return (
        <main id="main">
            <section className="hero">
                <div>
                    <span className="eyebrow">
                        READ IT. CHANGE IT. UNDERSTAND IT.
                    </span>
                    <h1>
                        Small examples.
                        <br />
                        <em>Real understanding.</em>
                    </h1>
                    <p>
                        Choose a language. Explore a concept. Make it your own
                        in an editor that gives you room to experiment.
                    </p>
                    <a className="primary" href="#curriculum">
                        Find your starting point <span>↗</span>
                    </a>
                </div>
                <div className="hero-code">
                    <div className="code-top">
                        <span>● ● ●</span>
                        <span>your-first-step.py</span>
                    </div>
                    <pre>
                        <span className="comment">
                            # Every programmer starts somewhere.
                        </span>
                        {"\n\n"}
                        <span className="purple">def</span> greet(name):{"\n"}{" "}
                        <span className="purple">return</span>{" "}
                        <span className="green">
                            f&quot;Hello, {"{name}"}!&quot;
                        </span>
                        {"\n\n"}print(greet(
                        <span className="green">&quot;curious mind&quot;</span>
                        ))
                    </pre>
                    <div className="code-output">
                        <span>OUTPUT</span>
                        <p>Hello, curious mind!</p>
                    </div>
                    <div className="code-note">
                        A little code. A new way to think.
                    </div>
                </div>
            </section>
            <section className="stats">
                <span>
                    <strong>6</strong> languages, one shared path
                </span>
                <span>
                    <strong>144</strong> bite-sized concept modules
                </span>
                <span>
                    <strong>96</strong> foundations exercises online
                </span>
            </section>
            <Explorer
                docs={catalog.docs.map(({ markdown, files, ...doc }) => doc)}
            />
        </main>
    );
}
