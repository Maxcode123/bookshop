BEGIN;
--
-- Add field authors to book
--
-- (no-op)
--
-- Alter field date_of_birth on author
--
ALTER TABLE "authors" ALTER COLUMN "date_of_birth" DROP NOT NULL;
COMMIT;
