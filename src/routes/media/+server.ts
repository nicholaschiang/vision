import { existsSync } from 'fs';
import { readFile, writeFile } from 'fs/promises';
import { join } from 'path';

export async function GET({ url, request }) {
	const media = new URL(url).searchParams.get('url');
	if (!media) {
		return new Response('No media URL provided', { status: 400 });
	}
	const mediaURL = new URL(media);

	const fileName = mediaURL.pathname.split('/').pop();
	if (!fileName) {
		return new Response('Invalid media URL', { status: 400 });
	}

	// To avoid hitting the Instagram API suspiciously, I cache media on disk.
	const file = join('/Users/nchiang/repos/vision/data/media', fileName);

	if (!existsSync(file)) {
		console.log('Downloading media', mediaURL);
		const headers = new Headers(request.headers);
		headers.set('referer', 'https://www.instagram.com/');
		headers.set('origin', 'https://www.instagram.com');
		headers.set('host', mediaURL.host);
		headers.set('sec-fetch-dest', 'image');
		headers.set('sec-fetch-mode', 'cors');
		headers.set('sec-fetch-site', 'cross-site');

		const arrayBuffer = await fetch(mediaURL, { headers })
			.then((response) => response.blob())
			.then((blob) => blob.arrayBuffer());
		await writeFile(file, Buffer.from(arrayBuffer));
	}

	console.log('Found existing media', file);
	const buffer = await readFile(file);
	return new Response(buffer);
}
