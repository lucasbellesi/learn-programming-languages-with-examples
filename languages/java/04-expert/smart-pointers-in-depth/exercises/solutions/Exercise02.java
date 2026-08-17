// Module focus: Observing cached values without keeping them alive.
// Why it matters: weak references are useful only when callers expect expiration.

import java.lang.ref.WeakReference;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Exercise02 {
    record CachedValue(String text) {
    }

    static final class WeakCache {
        private final Map<String, WeakReference<CachedValue>> entries = new HashMap<>();

        void store(String key, CachedValue value) {
            entries.put(key, new WeakReference<>(value));
        }

        void expireForDemo(String key) {
            WeakReference<CachedValue> reference = entries.get(key);
            if (reference != null) {
                reference.clear();
            }
        }

        void printLookup(String key) {
            WeakReference<CachedValue> reference = entries.get(key);
            if (reference == null) {
                System.out.println(key + ": missing");
                return;
            }

            CachedValue value = reference.get();
            if (value == null) {
                System.out.println(key + ": expired");
                return;
            }

            System.out.println(key + ": alive -> " + value.text());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String scenario = scanner.hasNextLine() ? scanner.nextLine() : "missing";
        WeakCache cache = new WeakCache();
        if (scenario.equals("missing")) {
            cache.printLookup("entry");
            return;
        }

        CachedValue value = new CachedValue("payload");
        cache.store("entry", value);
        if (scenario.equals("expired")) {
            cache.expireForDemo("entry");
        }
        cache.printLookup("entry");
    }
}
