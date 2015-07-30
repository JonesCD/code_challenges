diag <- read.csv("Patient_Diagnosis.csv")
treat <- read.csv("Patient_Treatment.csv")

diag_type <- table(diag$Diagnosis)
diag_type
