export function GET({ url, request }) {
	const media = new URL(url).searchParams.get('url');
	if (!media) {
		return new Response('No media URL provided', { status: 400 });
	}
	const mediaURL = new URL(media);
	const headers = new Headers(request.headers);
	headers.set('referer', 'https://www.instagram.com/');
	headers.set('origin', 'https://www.instagram.com');
	headers.set('host', mediaURL.host);
	headers.set('sec-fetch-dest', 'image');
	headers.set('sec-fetch-mode', 'cors');
	headers.set('sec-fetch-site', 'cross-site');
	return fetch(mediaURL, { headers });
}
