# copyright 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# copyright 2022 Hasa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Switzerland - PAIN Credit Transfer",
    "summary": "Generate ISO 20022 credit transfert (SEPA and not SEPA)",
    "version": "13.0.0.0.1",
    "category": "Finance",
    "author": "Hasa",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/l10n-switzerland",
    "depends": [
        "hasa_l10n_ch_pain_base",
        "l10n_ch_base_bank",
        "account_banking_sepa_credit_transfer",
    ],
    'installable': True,
}
