import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { useCallback } from "react";

export function useUrlSearchParams() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const getQueryParams = useCallback(
    (key: string) => {
      return searchParams.getAll(key);
    },
    [searchParams]
  );

  const setQueryParams = useCallback(
    (params: Record<string, string | undefined>) => {
      const newSearchParams = new URLSearchParams(searchParams.toString());
      Object.entries(params).forEach(([key, value]) => {
        if (value) newSearchParams.set(key, value);
        else newSearchParams.delete(key);
      });

      router.push(pathname + "?" + newSearchParams.toString());
    },
    [searchParams, pathname, router]
  );

  const appendQueryParams = useCallback(
    (params: Record<string, string | undefined>) => {
      const newSearchParams = new URLSearchParams(searchParams.toString());
      Object.entries(params).forEach(([key, value]) => {
        if (value) newSearchParams.append(key, value);
      });

      router.push(pathname + "?" + newSearchParams.toString());
    },
    [searchParams, pathname, router]
  );

  const deleteQueryParams = useCallback(
    (params: string[] | { key: string; value: string }[]) => {
      const newSearchParams = new URLSearchParams(searchParams.toString());
      params.forEach((param) => {
        if (typeof param == "string") {
          newSearchParams.delete(param);
        } else {
          newSearchParams.delete(param.key, param.value);
        }
      });

      router.push(pathname + "?" + newSearchParams.toString());
    },
    [searchParams, pathname, router]
  );

  return { getQueryParams, setQueryParams, appendQueryParams, deleteQueryParams };
}
