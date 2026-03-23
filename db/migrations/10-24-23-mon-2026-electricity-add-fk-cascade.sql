ALTER TABLE electricity
-- run this SHOW CREATE TABLE electricity to see foreign key
DROP FOREIGN KEY electricity_ibfk_1;
ALTER TABLE electricity
ADD CONSTRAINT fk_property
FOREIGN KEY (property)
REFERENCES properties(id)
ON DELETE CASCADE
ON UPDATE CASCADE;