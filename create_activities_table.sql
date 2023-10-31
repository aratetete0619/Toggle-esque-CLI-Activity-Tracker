CREATE TABLE activities (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255),
  start_date DATE,
  start_time TIME,
  end_date DATE,
  end_time TIME,
  duration TIME
);
