DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `taskId` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `containerCopies` int(4) NOT NULL,
  `imageList` varchar(255) NOT NULL,
  `specifyNode` varchar(255) NOT NULL,
  `compType` varchar(255) NOT NULL,
  `compNum` int(4) NOT NULL,
  `compMemory` varchar(16) NOT NULL,
  `createTime` datetime(6) DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`taskId`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `tasks` WRITE;
insert into `tasks`(`name`,`containerCopies`,`imageList`,`specifyNode`,`compType`,`compNum`,`compMemory`) values('task1',1,'ubuntu',4,'GPU',1,'200m');
UNLOCK TABLES;
