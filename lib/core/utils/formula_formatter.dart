/// Clean and convert LaTeX & chemical notation into legible Unicode symbols
/// for crisp, native mobile screen rendering without raw LaTeX artifacts.
class FormulaFormatter {
  static String format(String text) {
    if (text.isEmpty) return text;

    String res = text;

    // Remove LaTeX math delimiters $$ and $
    res = res.replaceAll(r'$$', '').replaceAll(r'$', '');

    // Common LaTeX arrow & symbol replacements
    res = res.replaceAll(r'\rightarrow', '→');
    res = res.replaceAll(r'\to', '→');
    res = res.replaceAll('->', '→');
    res = res.replaceAll('<=>', '⇌');
    res = res.replaceAll('<->', '↔');
    res = res.replaceAll(r'\xrightarrow{\Delta}', '—[Δ]→');
    res = res.replaceAll(r'\xrightarrow{\text{sunlight}}', '—[Sunlight]→');
    res = res.replaceAll(r'\xrightarrow{\text{Acid}}', '—[Acid]→');
    res = res.replaceAll(r'\xrightarrow', '→');
    res = res.replaceAll(r'\times', '×');
    res = res.replaceAll(r'\cdot', '·');
    res = res.replaceAll(r'\pm', '±');
    res = res.replaceAll(r'\le', '≤');
    res = res.replaceAll(r'\ge', '≥');
    res = res.replaceAll(r'\ne', '≠');
    res = res.replaceAll(r'\Delta', 'Δ');
    res = res.replaceAll(r'\alpha', 'α');
    res = res.replaceAll(r'\beta', 'β');
    res = res.replaceAll(r'\theta', 'θ');
    res = res.replaceAll(r'\pi', 'π');
    res = res.replaceAll(r'\rho', 'ρ');
    res = res.replaceAll(r'\mu', 'μ');
    res = res.replaceAll(r'\Sigma', 'Σ');
    res = res.replaceAll(r'\dots', '...');
    res = res.replaceAll(r'\sqrt', '√');
    res = res.replaceAll(r'\infty', '∞');
    res = res.replaceAll(r'^{\circ}', '°');
    res = res.replaceAll(r'^\circ', '°');
    res = res.replaceAll(r'\degree', '°');
    res = res.replaceAll(r'\circ', '°');

    // Remove \text{...} wrappers
    res = res.replaceAllMapped(RegExp(r'\\text\{([^}]*)\}'), (m) => m.group(1) ?? '');
    res = res.replaceAllMapped(RegExp(r'\\mathrm\{([^}]*)\}'), (m) => m.group(1) ?? '');
    res = res.replaceAllMapped(RegExp(r'\\mathbf\{([^}]*)\}'), (m) => m.group(1) ?? '');

    // Convert Superscripts
    res = res.replaceAll('^0', '⁰');
    res = res.replaceAll('^1', '¹');
    res = res.replaceAll('^2', '²');
    res = res.replaceAll('^3', '³');
    res = res.replaceAll('^4', '⁴');
    res = res.replaceAll('^5', '⁵');
    res = res.replaceAll('^6', '⁶');
    res = res.replaceAll('^7', '⁷');
    res = res.replaceAll('^8', '⁸');
    res = res.replaceAll('^9', '⁹');
    res = res.replaceAll('^+', '⁺');
    res = res.replaceAll('^-', '⁻');

    // Convert Subscripts
    res = res.replaceAll('_0', '₀');
    res = res.replaceAll('_1', '₁');
    res = res.replaceAll('_2', '₂');
    res = res.replaceAll('_3', '₃');
    res = res.replaceAll('_4', '₄');
    res = res.replaceAll('_5', '₅');
    res = res.replaceAll('_6', '₆');
    res = res.replaceAll('_7', '₇');
    res = res.replaceAll('_8', '₈');
    res = res.replaceAll('_9', '₉');

    // Clean up residual backslashes
    res = res.replaceAll(r'\,', ' ');
    res = res.replaceAll(r'\;', ' ');
    res = res.replaceAll(r'\quad', ' ');

    return res.trim();
  }
}
