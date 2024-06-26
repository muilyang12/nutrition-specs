import { ReactNode } from "react";
import PrintServiceName from "@components/PrintServiceName";
import "./global.css";

export const metadata = {
  title: "NutriInsights",
  description: "Help me to get insights about nutrition facts of foods.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <main>{children}</main>

        <PrintServiceName />
      </body>
    </html>
  );
}
