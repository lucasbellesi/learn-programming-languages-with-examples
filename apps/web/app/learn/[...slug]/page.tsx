import { notFound } from "next/navigation";
import Link from "next/link";
import { catalog, languages } from "@/lib/catalog";
import { Lesson } from "@/components/lesson";
export function generateStaticParams() {
    return catalog.docs.map((d) => ({ slug: d.id.split("/") }));
}
export async function generateMetadata({
    params,
}: {
    params: Promise<{ slug: string[] }>;
}) {
    const { slug } = await params;
    return {
        title:
            catalog.docs.find((d) => d.id === slug.join("/"))?.title ??
            "Not found",
    };
}
export default async function Page({
    params,
}: {
    params: Promise<{ slug: string[] }>;
}) {
    const { slug } = await params;
    const doc = catalog.docs.find((d) => d.id === slug.join("/"));
    if (!doc) notFound();
    return (
        <main id="main" className="lesson-page">
            <div className="breadcrumb">
                <Link href="/">Curriculum</Link>
                <span>/</span>
                <span>{languages[doc.language]}</span>
                <span>/</span>
                <span>{doc.level.slice(3)}</span>
            </div>
            <Lesson
                doc={doc}
                activities={doc.activities.map((id) => catalog.activities[id])}
                revision={catalog.revision}
            />
        </main>
    );
}
