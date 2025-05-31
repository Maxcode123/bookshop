BEGIN;
--
-- Delete model GenreNode
--
DROP TABLE "genre_nodes" CASCADE;
--
-- Remove field parent_id from genre
--
ALTER TABLE "genres" DROP COLUMN "parent_id" CASCADE;
--
-- Remove field root_id from genre
--
ALTER TABLE "genres" DROP COLUMN "root_id" CASCADE;
--
-- Add field path to genre
--
ALTER TABLE "genres" ADD COLUMN "path" ltree DEFAULT 'root' NOT NULL;
ALTER TABLE "genres" ALTER COLUMN "path" DROP DEFAULT;
COMMIT;
