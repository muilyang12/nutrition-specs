"use client";

import { useEffect } from "react";

export default function PrintServiceName() {
  useEffect(() => {
    console.log(`
┌────────────────────────────────────────────────────┐
│      _   _       _        _ _   _                  │
│     | \\ | |_   _| |_ _ __(_) |_(_) ___  _ __       │
│     |  \\| | | | | __| '__| | __| |/ _ \\| '_ \\      │
│     | |\\  | |_| | |_| |  | | |_| | (_) | | | |     │
│     |_|_\\_|\\__,_|\\__|_|  |_|\\__|_|\\___/|_| |_|     │
│     / ___| _ __   ___  ___ ___                     │
│     \\___ \\| '_ \\ / _ \\/ __/ __|                    │
│      ___) | |_) |  __/ (__\\__ \\                    │
│     |____/| .__/ \\___|\\___|___/                    │
│           |_|                                      │
└────────────────────────────────────────────────────┘
        `);
  }, []);

  return <></>;
}
