"use client";

import { useRouter } from "next/navigation";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import styles from "./CompareHeader.module.css";

export default function CompareHeader() {
  const router = useRouter();

  const handleClickBackButton = () => router.back();

  return (
    <div className={styles.compareHeaderWrapper}>
      <button onClick={handleClickBackButton}>
        <ArrowBackIcon />
      </button>
    </div>
  );
}
