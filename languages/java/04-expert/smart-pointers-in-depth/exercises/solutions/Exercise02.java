// Module focus: Observing cached values without keeping them alive.
// Why it matters: weak references are useful only when callers expect expiration.

import java.lang.ref.WeakReference;
import java.util.HashMap;
import java.util.Map;

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
        WeakCache cache = new WeakCache();
        CachedValue stable = new CachedValue("Still referenced");
        CachedValue temporary = new CachedValue("Short lived");

        cache.store("stable", stable);
        cache.store("temp", temporary);
        cache.printLookup("stable");
        cache.printLookup("temp");

        temporary = null;
        cache.expireForDemo("temp");

        cache.printLookup("stable");
        cache.printLookup("temp");
        cache.printLookup("missing");
    }
}
