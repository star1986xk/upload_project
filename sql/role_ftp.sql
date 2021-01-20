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

 Date: 13/01/2021 17:35:38
*/


-- ----------------------------
-- Table structure for role_ftp
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[role_ftp]') AND type IN ('U'))
	DROP TABLE [dbo].[role_ftp]
GO

CREATE TABLE [dbo].[role_ftp] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [role_id] int  NULL,
  [ftp_id] int  NULL
)
GO

ALTER TABLE [dbo].[role_ftp] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of role_ftp
-- ----------------------------
SET IDENTITY_INSERT [dbo].[role_ftp] ON
GO

INSERT INTO [dbo].[role_ftp] ([id], [role_id], [ftp_id]) VALUES (N'1', N'1', N'1')
GO

SET IDENTITY_INSERT [dbo].[role_ftp] OFF
GO


-- ----------------------------
-- Auto increment value for role_ftp
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[role_ftp]', RESEED, 12)
GO


-- ----------------------------
-- Primary Key structure for table role_ftp
-- ----------------------------
ALTER TABLE [dbo].[role_ftp] ADD CONSTRAINT [PK__role_ftp__3213E83F0C50D423] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

