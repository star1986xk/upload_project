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

 Date: 13/01/2021 17:33:28
*/


-- ----------------------------
-- Table structure for ftp
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[ftp]') AND type IN ('U'))
	DROP TABLE [dbo].[ftp]
GO

CREATE TABLE [dbo].[ftp] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [name] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [ip] nvarchar(16) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [port] nvarchar(6) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [username] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [password] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [path] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[ftp] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of ftp
-- ----------------------------
SET IDENTITY_INSERT [dbo].[ftp] ON
GO

INSERT INTO [dbo].[ftp] ([id], [name], [ip], [port], [username], [password], [path]) VALUES (N'1', N'中转服务器', N'yun.fjhczsgc.com', N'21', N'test', N'Hh@121212', N'/test/中转站')
GO

INSERT INTO [dbo].[ftp] ([id], [name], [ip], [port], [username], [password], [path]) VALUES (N'2', N'上传服务器', N'yun.fjhczsgc.com', N'21', N'test', N'Hh@121212', N'/test/NAS')
GO

SET IDENTITY_INSERT [dbo].[ftp] OFF
GO


-- ----------------------------
-- Auto increment value for ftp
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[ftp]', RESEED, 2)
GO


-- ----------------------------
-- Primary Key structure for table ftp
-- ----------------------------
ALTER TABLE [dbo].[ftp] ADD CONSTRAINT [PK_ftp] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

