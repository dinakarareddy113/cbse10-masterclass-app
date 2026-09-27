import 'package:flutter/foundation.dart';

@immutable
class FormulaCard {
  final String chapterId;
  final String chapterTitle;
  final String summary;
  final List<String> formulas;

  const FormulaCard({
    required this.chapterId,
    required this.chapterTitle,
    required this.summary,
    required this.formulas,
  });

  factory FormulaCard.fromMap(Map<String, dynamic> map) {
    return FormulaCard(
      chapterId: map['id'] as String? ?? '',
      chapterTitle: map['title'] as String? ?? '',
      summary: map['summary'] as String? ?? '',
      formulas: List<String>.from(map['formulas'] as List? ?? []),
    );
  }
}

@immutable
class RayDiagramItem {
  final String title;
  final String positionObject;
  final String positionImage;
  final String natureImage;
  final String magnification;
  final String application;
  final String asciiRay;

  const RayDiagramItem({
    required this.title,
    required this.positionObject,
    required this.positionImage,
    required this.natureImage,
    required this.magnification,
    required this.application,
    required this.asciiRay,
  });

  factory RayDiagramItem.fromMap(Map<String, dynamic> map) {
    return RayDiagramItem(
      title: map['title'] as String? ?? '',
      positionObject: map['position_object'] as String? ?? '',
      positionImage: map['position_image'] as String? ?? '',
      natureImage: map['nature_image'] as String? ?? '',
      magnification: map['magnification'] as String? ?? '',
      application: map['application'] as String? ?? '',
      asciiRay: map['ascii_ray'] as String? ?? '',
    );
  }
}

@immutable
class ChemistryEquationItem {
  final String reactionType;
  final String equation;
  final String reactants;
  final String products;
  final String observation;

  const ChemistryEquationItem({
    required this.reactionType,
    required this.equation,
    required this.reactants,
    required this.products,
    required this.observation,
  });

  factory ChemistryEquationItem.fromMap(Map<String, dynamic> map) {
    return ChemistryEquationItem(
      reactionType: map['reaction_type'] as String? ?? '',
      equation: map['equation'] as String? ?? '',
      reactants: map['reactants'] as String? ?? '',
      products: map['products'] as String? ?? '',
      observation: map['observation'] as String? ?? '',
    );
  }
}

@immutable
class HistoricalEventItem {
  final String year;
  final String title;
  final String description;

  const HistoricalEventItem({
    required this.year,
    required this.title,
    required this.description,
  });

  factory HistoricalEventItem.fromMap(Map<String, dynamic> map) {
    return HistoricalEventItem(
      year: map['year'] as String? ?? '',
      title: map['title'] as String? ?? '',
      description: map['description'] as String? ?? '',
    );
  }
}
