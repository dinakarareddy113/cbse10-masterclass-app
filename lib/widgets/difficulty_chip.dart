import 'package:flutter/material.dart';
import '../models/question.dart';

class DifficultyChip extends StatelessWidget {
  final DifficultyLevel level;

  const DifficultyChip({super.key, required this.level});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: level.badgeColor.withOpacity(0.12),
        borderRadius: BorderRadius.circular(6),
        border: Border.all(
          color: level.badgeColor.withOpacity(0.4),
          width: 1,
        ),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            level == DifficultyLevel.hots ? Icons.local_fire_department : Icons.speed,
            size: 13,
            color: level.badgeColor,
          ),
          const SizedBox(width: 4),
          Text(
            level.label,
            style: TextStyle(
              fontSize: 11,
              fontWeight: FontWeight.w700,
              color: level.badgeColor,
              letterSpacing: 0.2,
            ),
          ),
        ],
      ),
    );
  }
}
