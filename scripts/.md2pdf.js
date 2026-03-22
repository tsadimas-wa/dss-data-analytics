module.exports = {
	stylesheet: [],
	css: `.mermaid { background: white; }`,
	body_class: [],
	marked_extensions: [],
	pdf_options: {
		format: 'A4',
		margin: { top: '20mm', bottom: '20mm', left: '20mm', right: '20mm' },
	},
	script: [
		{ url: 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js' },
	],
	marked_options: {},
	launch_options: {},
};
