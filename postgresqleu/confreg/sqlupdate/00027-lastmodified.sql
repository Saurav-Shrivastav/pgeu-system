ALTER TABLE confreg_conferenceregistration ADD COLUMN lastmodified timestamptz;
UPDATE confreg_conferenceregistration SET lastmodified=created;