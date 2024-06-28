import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { useCallback } from "react";

export function useUrlSearchParams() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const setQueryParams = useCallback(
    (params: Record<string, string | undefined>) => {
      const newSearchParams = new URLSearchParams(searchParams.toString());
      Object.entries(params).map(([key, value]) => {
        if (value) newSearchParams.set(key, value);
        else newSearchParams.delete(key);
      });

      router.push(pathname + "?" + newSearchParams.toString());
    },
    [searchParams]
  );

  return { setQueryParams };
}
