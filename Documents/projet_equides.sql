-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 07 sep. 2022 à 11:59
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_equides`
--

-- --------------------------------------------------------

--
-- Structure de la table `centres_detention`
--

DROP TABLE IF EXISTS `centres_detention`;
CREATE TABLE IF NOT EXISTS `centres_detention` (
  `Id_centre` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_centre` varchar(64) DEFAULT NULL,
  `Type_activite_centre` varchar(64) DEFAULT NULL,
  `Telephone_centre` varchar(14) DEFAULT NULL,
  `Mail_centre` varchar(50) DEFAULT NULL,
  `Raison_Sociale_centre` varchar(70) DEFAULT NULL,
  `Ligne1_Adresse_centre` mediumtext,
  `Ligne2_Adresse_centre` mediumtext,
  `Code_postal_centre` varchar(5) DEFAULT NULL,
  `Ville_centre` varchar(45) DEFAULT NULL,
  `Pays_centre` varchar(64) DEFAULT NULL,
  `Numero_SIRET_det_centre` varchar(15) DEFAULT NULL,
  `Statut_juridique_centre` varchar(35) DEFAULT NULL,
  `Code_APE_det_centre` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Id_centre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `centres_detention`
--

INSERT INTO `centres_detention` (`Id_centre`, `Nom_centre`, `Type_activite_centre`, `Telephone_centre`, `Mail_centre`, `Raison_Sociale_centre`, `Ligne1_Adresse_centre`, `Ligne2_Adresse_centre`, `Code_postal_centre`, `Ville_centre`, `Pays_centre`, `Numero_SIRET_det_centre`, `Statut_juridique_centre`, `Code_APE_det_centre`) VALUES
(1, 'Elevage de la Palouse', 'Elevage de chevaux (races américaines)', '0650674454', 'elevage@lapalouse.fr', 'Elevage de la Palouse', '20 rue saint Florentin', NULL, '54115', 'GELAUCOURT', 'France', '48366452000028', NULL, '0143Z');

-- --------------------------------------------------------

--
-- Structure de la table `deplacements`
--

DROP TABLE IF EXISTS `deplacements`;
CREATE TABLE IF NOT EXISTS `deplacements` (
  `id_dep` int(11) NOT NULL,
  `id_transport` int(11) DEFAULT NULL,
  `id_eq_dep` int(11) DEFAULT NULL,
  `date_depart_dep` datetime DEFAULT NULL,
  `date_arrive_dep` datetime DEFAULT NULL,
  `lieu_depart_dep` varchar(45) DEFAULT NULL,
  `lieu_arrive_dep` varchar(45) DEFAULT NULL,
  `motif_depart_dep` varchar(50) DEFAULT NULL,
  `motif_arrive_dep` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_dep`),
  KEY `id_transport` (`id_transport`),
  KEY `id_eq_dep` (`id_eq_dep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `deplacements`
--

INSERT INTO `deplacements` (`id_dep`, `id_transport`, `id_eq_dep`, `date_depart_dep`, `date_arrive_dep`, `lieu_depart_dep`, `lieu_arrive_dep`, `motif_depart_dep`, `motif_arrive_dep`) VALUES
(2, 1, 5, '2022-08-20 00:00:00', '2022-08-22 00:00:00', 'Paris', 'Nancy', 'Achat', 'Installation'),
(3, 1, 8, '2022-08-20 00:00:00', '2022-08-21 00:00:00', 'Paris', 'Reims', 'Recupération', 'Retour Expo'),
(4, 1, 9, '2022-08-21 00:00:00', '2022-08-22 00:00:00', 'Reims', 'Nancy', 'Fin compet', 'Retour Maison');

-- --------------------------------------------------------

--
-- Structure de la table `equides`
--

DROP TABLE IF EXISTS `equides`;
CREATE TABLE IF NOT EXISTS `equides` (
  `id_eq` int(11) NOT NULL AUTO_INCREMENT,
  `centre_eq` int(11) DEFAULT NULL,
  `type_eq` int(11) DEFAULT NULL,
  `race_eq` int(11) DEFAULT NULL,
  `nom_eq` varchar(50) DEFAULT NULL,
  `sexe_eq` bit(1) DEFAULT NULL,
  `puce_eq` bigint(20) DEFAULT NULL,
  `sire_eq` varchar(10) DEFAULT NULL,
  `pere_eq` varchar(25) DEFAULT NULL,
  `mere_eq` varchar(25) DEFAULT NULL,
  `pere_mere_eq` varchar(25) DEFAULT NULL,
  `num_stu_book_eq` varchar(64) DEFAULT NULL,
  `id_prop_eq` int(11) DEFAULT NULL,
  `description_eq` mediumtext,
  PRIMARY KEY (`id_eq`),
  KEY `centre_eq` (`centre_eq`),
  KEY `id_prop_eq` (`id_prop_eq`),
  KEY `type_eq` (`type_eq`),
  KEY `race_eq` (`race_eq`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `equides`
--

INSERT INTO `equides` (`id_eq`, `centre_eq`, `type_eq`, `race_eq`, `nom_eq`, `sexe_eq`, `puce_eq`, `sire_eq`, `pere_eq`, `mere_eq`, `pere_mere_eq`, `num_stu_book_eq`, `id_prop_eq`, `description_eq`) VALUES
(4, 1, 4, 1, 'DL SHEZA PEPPYS MATCH', b'1', 956000008824673, '504444150B', 'PEPPY PINE TAUR', 'MEX AND MATCH', 'CUPIDS POOL BAR', 'APHA #1025922', 2, NULL),
(5, 1, 4, 2, 'DL SPIRIT IN TOWN', b'0', 981100004180661, 'En cours', 'MEET ME DOWNTOWN', 'BF BOOS N SPIRITS', 'A BEAR SPIRIT', 'APHA #1052253', 2, NULL),
(6, 1, 4, 3, 'EL SNOW ROMAN ZIPPO', b'0', NULL, '15197398N', 'THREEZIPS ANDYOUROUT', 'RUBY ROMAN STRAW', 'TOBYS WAKAN TANKA', 'APHC #678408', 2, NULL),
(7, 1, 4, 2, 'EL MIS DOWNTOWN BLUE', b'1', 250258500144575, 'En cours', 'MEET ME DOWNTOWN', 'MISS BLUE MIDWAY', 'MIDWAY STYLE', 'APHC #678408', 2, NULL),
(8, 1, 4, 1, 'EL RED SAN BADGER', b'1', 250258500144741, 'En cours', 'BR RED HOT CHILI PEP', 'RED BOUBA', 'DOCS FUTURELIGHT', 'AQHA #5770933', 2, NULL),
(9, 1, 4, 1, 'MEET ME DOWNTOWN', b'0', 956000008926192, '60033601K', 'MR BE DOWNTOWN', 'RITZY REVIEW', 'IMPRESSIVE REVIEW', 'AQHA #4035738 PHBA #Q4035738', 2, NULL),
(10, 1, 4, 2, 'MISS BLUE MIDWAY', b'1', 956000003336012, '50450414S', 'MIDWAY STYLE', 'MISS BLUE BREEZE', 'DOCTOR BLUE', 'APHA #735112', 2, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `evenements`
--

DROP TABLE IF EXISTS `evenements`;
CREATE TABLE IF NOT EXISTS `evenements` (
  `id_even` int(11) NOT NULL,
  `id_eq_even` int(11) DEFAULT NULL,
  `date_even` datetime DEFAULT NULL,
  `titre_even` varchar(64) DEFAULT NULL,
  `detail_even` mediumtext,
  PRIMARY KEY (`id_even`),
  KEY `id_eq_even` (`id_eq_even`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `evenements`
--

INSERT INTO `evenements` (`id_even`, `id_eq_even`, `date_even`, `titre_even`, `detail_even`) VALUES
(1, 4, '2022-09-08 00:00:00', 'Rencontre avec le CESI', 'SUPER');

-- --------------------------------------------------------

--
-- Structure de la table `prestataires`
--

DROP TABLE IF EXISTS `prestataires`;
CREATE TABLE IF NOT EXISTS `prestataires` (
  `id_presta` int(11) NOT NULL AUTO_INCREMENT,
  `type_presta` int(11) DEFAULT NULL,
  `nom_presta` varchar(255) DEFAULT NULL,
  `prenom_presta` varchar(255) DEFAULT NULL,
  `tel_presta` varchar(255) DEFAULT NULL,
  `mail_presta` varchar(255) DEFAULT NULL,
  `adresse_ligne_1_presta` varchar(255) DEFAULT NULL,
  `adresse_ligne_2_presta` varchar(255) DEFAULT NULL,
  `cp_presta` varchar(255) DEFAULT NULL,
  `ville_presta` varchar(255) DEFAULT NULL,
  `pays_presta` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_presta`),
  KEY `type_presta` (`type_presta`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `prestataires`
--

INSERT INTO `prestataires` (`id_presta`, `type_presta`, `nom_presta`, `prenom_presta`, `tel_presta`, `mail_presta`, `adresse_ligne_1_presta`, `adresse_ligne_2_presta`, `cp_presta`, `ville_presta`, `pays_presta`) VALUES
(1, 1, 'Dr LAURENT', 'Guy', '03 83 26 28 85', NULL, NULL, NULL, NULL, NULL, NULL),
(2, 2, 'DUNCKEL', 'Thierry', '06 21 65 09 61', NULL, NULL, NULL, NULL, NULL, NULL),
(3, 1, 'LAIDELLI', 'Emmanuel', '06 50 67 44 54', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `proprietaires`
--

DROP TABLE IF EXISTS `proprietaires`;
CREATE TABLE IF NOT EXISTS `proprietaires` (
  `id_prop` int(11) NOT NULL,
  `nom_prop` varchar(30) DEFAULT NULL,
  `prenom_prop` varchar(30) DEFAULT NULL,
  `sire_prop` varchar(15) DEFAULT NULL,
  `siret_prop` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`id_prop`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `proprietaires`
--

INSERT INTO `proprietaires` (`id_prop`, `nom_prop`, `prenom_prop`, `sire_prop`, `siret_prop`) VALUES
(2, 'LAIDELLI', 'Emmanuel', '541158253412', '48366452000028');

-- --------------------------------------------------------

--
-- Structure de la table `races_equides`
--

DROP TABLE IF EXISTS `races_equides`;
CREATE TABLE IF NOT EXISTS `races_equides` (
  `id_race` int(11) NOT NULL AUTO_INCREMENT,
  `id_type_eq` int(11) DEFAULT NULL,
  `nom_race` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id_race`),
  KEY `id_type_eq` (`id_type_eq`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `races_equides`
--

INSERT INTO `races_equides` (`id_race`, `id_type_eq`, `nom_race`) VALUES
(1, 4, 'Quarter Horse'),
(2, 4, 'Paint Horse'),
(3, 4, 'Appaloosa'),
(4, 6, 'Baudet du Poitou'),
(5, 6, 'Âne de Provence'),
(6, 6, 'Âne du Cotentin'),
(7, 5, 'Shetland'),
(8, 5, 'Connemara'),
(9, 5, 'Poney Welsh');

-- --------------------------------------------------------

--
-- Structure de la table `soins`
--

DROP TABLE IF EXISTS `soins`;
CREATE TABLE IF NOT EXISTS `soins` (
  `id_soin` int(11) NOT NULL AUTO_INCREMENT,
  `id_type_soin` int(11) DEFAULT NULL,
  `nom_soin` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id_soin`),
  KEY `id_type_soin` (`id_type_soin`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `soins`
--

INSERT INTO `soins` (`id_soin`, `id_type_soin`, `nom_soin`) VALUES
(1, 1, 'Strongid'),
(2, 1, 'Eqvalen'),
(3, 1, 'Equimax'),
(4, 1, 'Panacur'),
(5, 1, 'Eraquell'),
(6, 1, 'Equest'),
(7, 1, 'Panacur'),
(8, 1, 'Eqvalan duo'),
(9, 1, 'Hippomectine'),
(10, 2, 'Actiferm recovry flash'),
(11, 3, 'Rhinopneumonie'),
(12, 3, 'Tétanos'),
(13, 3, 'Grippe'),
(14, 3, 'Rage');

-- --------------------------------------------------------

--
-- Structure de la table `soins_equides`
--

DROP TABLE IF EXISTS `soins_equides`;
CREATE TABLE IF NOT EXISTS `soins_equides` (
  `id_soin_eq` int(11) NOT NULL AUTO_INCREMENT,
  `id_eq_soin` int(11) DEFAULT NULL,
  `id_type_soin` int(11) DEFAULT NULL,
  `id_soin` int(11) DEFAULT NULL,
  `id_prestataire` int(11) DEFAULT NULL,
  `date_soin` datetime DEFAULT NULL,
  `ref_soin` varchar(255) DEFAULT NULL,
  `com_soin` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_soin_eq`),
  KEY `id_eq_soin` (`id_eq_soin`),
  KEY `id_type_soin` (`id_type_soin`),
  KEY `id_soin` (`id_soin`),
  KEY `id_prestataire` (`id_prestataire`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `soins_equides`
--

INSERT INTO `soins_equides` (`id_soin_eq`, `id_eq_soin`, `id_type_soin`, `id_soin`, `id_prestataire`, `date_soin`, `ref_soin`, `com_soin`) VALUES
(4, 4, 3, 13, 1, '2022-09-01 00:00:00', 'EEEOZOZEOZ', 'RAS');

-- --------------------------------------------------------

--
-- Structure de la table `types_equides`
--

DROP TABLE IF EXISTS `types_equides`;
CREATE TABLE IF NOT EXISTS `types_equides` (
  `id_type_eq` int(11) NOT NULL AUTO_INCREMENT,
  `nom_type_eq` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`id_type_eq`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `types_equides`
--

INSERT INTO `types_equides` (`id_type_eq`, `nom_type_eq`) VALUES
(4, 'Cheval'),
(5, 'Poney'),
(6, 'Âne');

-- --------------------------------------------------------

--
-- Structure de la table `types_prestataires`
--

DROP TABLE IF EXISTS `types_prestataires`;
CREATE TABLE IF NOT EXISTS `types_prestataires` (
  `Id_type_presta` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_type_presta` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Id_type_presta`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `types_prestataires`
--

INSERT INTO `types_prestataires` (`Id_type_presta`, `Nom_type_presta`) VALUES
(1, 'Médical'),
(2, 'Maréchal ferrant');

-- --------------------------------------------------------

--
-- Structure de la table `types_soins`
--

DROP TABLE IF EXISTS `types_soins`;
CREATE TABLE IF NOT EXISTS `types_soins` (
  `id_type_soin` int(11) NOT NULL AUTO_INCREMENT,
  `nom_type_soin` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_type_soin`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `types_soins`
--

INSERT INTO `types_soins` (`id_type_soin`, `nom_type_soin`) VALUES
(1, 'Vermifuge'),
(2, 'Traitement'),
(3, 'Vaccin');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `id_centre_user` int(11) DEFAULT NULL,
  `login_user` varchar(20) DEFAULT NULL,
  `code_user` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  KEY `id_centre_user` (`id_centre_user`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id_user`, `id_centre_user`, `login_user`, `code_user`) VALUES
(4, 1, 'emmanuel', NULL);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `deplacements`
--
ALTER TABLE `deplacements`
  ADD CONSTRAINT `deplacements_ibfk_1` FOREIGN KEY (`id_eq_dep`) REFERENCES `equides` (`id_eq`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `equides`
--
ALTER TABLE `equides`
  ADD CONSTRAINT `equides_ibfk_1` FOREIGN KEY (`centre_eq`) REFERENCES `centres_detention` (`Id_centre`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `equides_ibfk_2` FOREIGN KEY (`id_prop_eq`) REFERENCES `proprietaires` (`id_prop`),
  ADD CONSTRAINT `equides_ibfk_3` FOREIGN KEY (`type_eq`) REFERENCES `types_equides` (`id_type_eq`) ON UPDATE CASCADE,
  ADD CONSTRAINT `equides_ibfk_4` FOREIGN KEY (`race_eq`) REFERENCES `races_equides` (`id_race`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `evenements`
--
ALTER TABLE `evenements`
  ADD CONSTRAINT `evenements_ibfk_1` FOREIGN KEY (`id_eq_even`) REFERENCES `equides` (`id_eq`);

--
-- Contraintes pour la table `prestataires`
--
ALTER TABLE `prestataires`
  ADD CONSTRAINT `prestataires_ibfk_1` FOREIGN KEY (`type_presta`) REFERENCES `types_prestataires` (`Id_type_presta`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `races_equides`
--
ALTER TABLE `races_equides`
  ADD CONSTRAINT `races_equides_ibfk_1` FOREIGN KEY (`id_type_eq`) REFERENCES `types_equides` (`id_type_eq`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `soins`
--
ALTER TABLE `soins`
  ADD CONSTRAINT `soins_ibfk_1` FOREIGN KEY (`id_type_soin`) REFERENCES `types_soins` (`id_type_soin`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `soins_equides`
--
ALTER TABLE `soins_equides`
  ADD CONSTRAINT `soins_equides_ibfk_1` FOREIGN KEY (`id_eq_soin`) REFERENCES `equides` (`id_eq`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `soins_equides_ibfk_2` FOREIGN KEY (`id_soin`) REFERENCES `soins` (`id_soin`),
  ADD CONSTRAINT `soins_equides_ibfk_3` FOREIGN KEY (`id_prestataire`) REFERENCES `prestataires` (`id_presta`) ON UPDATE CASCADE,
  ADD CONSTRAINT `soins_equides_ibfk_4` FOREIGN KEY (`id_type_soin`) REFERENCES `types_soins` (`id_type_soin`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`id_centre_user`) REFERENCES `centres_detention` (`Id_centre`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
