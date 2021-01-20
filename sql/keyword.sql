/*
 Navicat Premium Data Transfer

 Source Server         : SQLserver单位服务器
 Source Server Type    : SQL Server
 Source Server Version : 10506000
 Source Host           : 101.200.47.16:1433
 Source Catalog        : test
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 10506000
 File Encoding         : 65001

 Date: 20/01/2021 11:05:14
*/


-- ----------------------------
-- Table structure for keyword
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[keyword]') AND type IN ('U'))
	DROP TABLE [dbo].[keyword]
GO

CREATE TABLE [dbo].[keyword] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [word] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [user_id] int  NULL
)
GO

ALTER TABLE [dbo].[keyword] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Auto increment value for keyword
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[keyword]', RESEED, 3)
GO


-- ----------------------------
-- Primary Key structure for table keyword
-- ----------------------------
ALTER TABLE [dbo].[keyword] ADD CONSTRAINT [PK__keyword__3213E83F10216507] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

