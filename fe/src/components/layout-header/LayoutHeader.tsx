"use client";

import { useRouter } from "next/navigation";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import styles from "./LayoutHeader.module.css";

export default function LayoutHeader() {
  const router = useRouter();

  const handleClickBackButton = () => router.back();

  return (
    <div className={styles.layoutHeaderWrapper}>
      <button onClick={handleClickBackButton}>
        <ArrowBackIcon />
      </button>
    </div>
  );
}