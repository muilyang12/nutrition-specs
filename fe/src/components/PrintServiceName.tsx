"use client";

import { useEffect } from "react";

export default function PrintServiceName() {
  useEffect(() => {
    console.log(`
┌──────────────────────────────────┐
│      _   _       _        _      │
│     | \\ | |_   _| |_ _ __(_)     │
│     |  \\| | | | | __| '__| |     │
│     | |\\  | |_| | |_| |  | |     │
│     |_|_\\_|\\__,_|\\__|_|  |_|     │
│     / ___| _ __   ___  ___       │
│     \\___ \\| '_ \\ / _ \\/ __|      │
│      ___) | |_) |  __/ (__       │
│     |____/| .__/ \\___|\\___|      │
│           |_|                    │
└──────────────────────────────────┘
        `);
  }, []);

  return <></>;
}
