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

 Date: 20/01/2021 15:13:29
*/


-- ----------------------------
-- Table structure for info
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[info]') AND type IN ('U'))
	DROP TABLE [dbo].[info]
GO

CREATE TABLE [dbo].[info] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [title] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [describe] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [tips1] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [tips2] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[info] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of info
-- ----------------------------
SET IDENTITY_INSERT [dbo].[info] ON
GO

INSERT INTO [dbo].[info] ([id], [title], [describe], [tips1], [tips2]) VALUES (N'1', N'项目上传工具', N'请上传文件！
    谢谢！', N'提示1111', N'提示22222')
GO

SET IDENTITY_INSERT [dbo].[info] OFF
GO


-- ----------------------------
-- Auto increment value for info
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[info]', RESEED, 1)
GO


-- ----------------------------
-- Primary Key structure for table info
-- ----------------------------
ALTER TABLE [dbo].[info] ADD CONSTRAINT [PK_info] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

