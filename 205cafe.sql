-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 19, 2018 at 09:27 PM
-- Server version: 5.7.21-0ubuntu0.16.04.1
-- PHP Version: 7.0.25-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205cafe`
--

-- --------------------------------------------------------

--
-- Table structure for table `userInfo`
--

CREATE TABLE `userInfo` (
  `ID` int(8) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `integral` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userInfo`
--

INSERT INTO `userInfo` (`ID`, `username`, `password`, `email`, `integral`) VALUES
(1000, 'abc', '123', 'abc@gmail.com', 0),
(1048, 'abcdefgh', '12345678', 'abc@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `user_question`
--

CREATE TABLE `user_question` (
  `qID` int(11) NOT NULL,
  `questioner` varchar(30) DEFAULT NULL,
  `questioner-email` varchar(30) DEFAULT NULL,
  `question` varchar(200) DEFAULT NULL,
  `question-date` date DEFAULT NULL,
  `Done?` enum('yes','no') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_question`
--

INSERT INTO `user_question` (`qID`, `questioner`, `questioner-email`, `question`, `question-date`, `Done?`) VALUES
(1, 'example', 'example@gmail.com', 'hello', '2018-03-04', 'no'),
(7, 'John', 'john@yahoo.com.hk', 'Where is your coffee shop?', '2018-03-18', 'no');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `userInfo`
--
ALTER TABLE `userInfo`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `user_question`
--
ALTER TABLE `user_question`
  ADD PRIMARY KEY (`qID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `userInfo`
--
ALTER TABLE `userInfo`
  MODIFY `ID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1049;
--
-- AUTO_INCREMENT for table `user_question`
--
ALTER TABLE `user_question`
  MODIFY `qID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
