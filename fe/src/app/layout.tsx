import { Noto_Sans_KR } from "next/font/google";
import { ReactNode } from "react";
import Modal from "@components/modal/Modal";
import PrintServiceName from "@components/PrintServiceName";
import "./global.css";

export const metadata = {
  title: "NutriSpec",
  description: "Help me to get insights about nutrition facts of foods.",
};

const notoSansKr = Noto_Sans_KR({
  subsets: ["latin"],
  weight: ["100", "400", "700"],
});

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className={notoSansKr.className}>
        <main>{children}</main>

        <Modal />

        <PrintServiceName />
      </body>
    </html>
  );
}
